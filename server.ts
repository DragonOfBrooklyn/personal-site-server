import Anthropic from '@anthropic-ai/sdk';
import { type MessageParam } from '@anthropic-ai/sdk/resources/messages.mjs';
import { Pinecone } from '@pinecone-database/pinecone';

const pinecone = new Pinecone({ 
    apiKey: process.env.PINECONE_API_KEY ?? ''
});
const pcindex = pinecone.index("personal-site-data");

const CORS_HEADERS = {
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'OPTIONS, POST',
    'Access-Control-Allow-Headers': 'Content-Type, jlong-authorization',
  }
}

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});
async function callClaude(
  convo: MessageParam[], 
  query: string, 
  retry: boolean = true){
  const timezoneOption = {timeZone: "America/New_York"};
  let queryEmbeddings_res, vectorSearchResponse, queryEmbeddings, claude_res;
  if(!retry) console.log(`retrying at ${new Date().toLocaleTimeString('en-US', timezoneOption)}`);
  try {
    queryEmbeddings_res = await fetch('https://api.voyageai.com/v1/embeddings',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.VOYAGE_API_KEY}`
      },
      body: JSON.stringify({
        "input": [query],
        "model": "voyage-large-2",
        "input_type": "query"
      })
    });
    queryEmbeddings = await queryEmbeddings_res.json();
  }catch (err){
    if(retry) return callClaude(convo, query, false);
    return [{
      type: "error", 
      text: "I'm having difficulty making your question relatable to Jordan and his background, I'll have to contact him about this... Feel free to ask me other questions about Jordan"
    }];
  }
  try{
    vectorSearchResponse = await pcindex.query({
      topK: 4,
      //@ts-ignore
      vector: queryEmbeddings.data[0].embedding,
      includeMetadata: true
    });
  }catch (err){
    if(retry) return callClaude(convo, query, false);
    return [{
      type: "error", 
      text: "I'm having difficulty referencing Jordan's background, I'll have to contact him about this... Feel free to ask me other questions about Jordan"
    }];
  }
  let retrievedDocuments = '';
  try{
    if(typeof vectorSearchResponse === 'undefined') throw new Error('No vector matches');
    for await(const {metadata} of vectorSearchResponse.matches){
      if(!metadata) continue;
      retrievedDocuments = retrievedDocuments + ' ' + metadata['originaltext'];
    }
  }catch (err){
    if(retry) return callClaude(convo, query, false);
    return [{
      type: "error", 
      text: "I'm having difficulty referencing some of Jordan's background, I'll have to contact him about this... Feel free to ask me other questions about Jordan"
    }];
  }
  try{
    claude_res = await anthropic.messages.create({
      max_tokens: 500,
      //no longer sends the old conversation, this api either doesn't accept sending entire conversations or has a bug that doesn't accept an array of messages
      messages: [{"role": "user", "content": `Based on this information: '${retrievedDocuments ?? 'No additional information relevant to Jordan'}', generate a response to the this question: ${query}`}],
      model: 'claude-3-opus-20240229',
      system: `You should only respond with known information about Jordan Long. 
      Restrict information that cannot be legally asked during an interview 
      such as race, color, religion, sex, national origin, or age. Try to limit your responses to no more than two paragraph.
      If any referenced information uses the first person like I or me, please replace with Jordan, he, or him.
      Avoid referencing the information provided and just speak as if you were talking about a friend.
      If irrelevant information to Jordan is asked, please comprehend the topic of the question and answer with similar info about Jordan.
      For example, if asked how tall is mount everest, Jordan likes the outdoors so you can reference his relevant hobbies instead.
      Another example is if asked about a restaurant, you can reference his relevant cooking and baking hobbies.
      Lastly, if the question is completely irrelevant to any of Jordan's information, respond with a fun fact about Jordan.
      `,
      temperature: 0,
    });
  }catch (err){
    if(retry) return callClaude(convo, query, false);
    return [{
      type: "error", 
      text: "I'm having difficulty referencing Jordan's background with your question, I'll have to contact him about this... Feel free to ask me other questions about Jordan"
    }];
  }
  return claude_res.content;
}

Bun.serve({
  port: process.env.PORT,
  async fetch(request: Request) {
    const { method, headers, body } = request;
    //CORS preflight response
    if (method === 'OPTIONS') {
      console.log('CORS pre-flight response');
      return new Response('Departed', CORS_HEADERS);
    }
    //creating response headers
    const responseHeaders = new Headers();
    responseHeaders.set('Access-Control-Allow-Origin', '*');
    responseHeaders.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    //checking authorization
    if(headers.get('jlong-authorization') !== 'PersonalSiteForJordanLong'){
      console.log('unknown authorization - incorrect header');
      return new Response('Unknown Authorization', {headers: responseHeaders});
    }
    //request handling and response
    if(method === 'POST' && body){
      responseHeaders.set('Content-Type','application/json');
      const fullConversation = await Bun.readableStreamToJSON(body);
      const claudeAnswer = callClaude(fullConversation.oldConversation, fullConversation.query)
      .then((val) => {
        return new Response(JSON.stringify(val[0]), {headers: responseHeaders})
      });
      return claudeAnswer;
    }
    //response handling
    return new Response('Incorrect type of request', {headers: responseHeaders});     
  }
})

console.log(`listening on port ${process.env.PORT}...`); //not in Lambda call
