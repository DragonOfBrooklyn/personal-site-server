import Anthropic from '@anthropic-ai/sdk';
import { type MessageParam } from '@anthropic-ai/sdk/resources/messages.mjs';

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
async function callClaude(convo: MessageParam[]){
  const message = await anthropic.messages.create({
    max_tokens: 100,
    messages: convo,
    model: 'claude-3-haiku-20240307',
    system: 'You should only respond with known information about Jordan Long. Restrict information that cannot be legally asked during an interview such as race, color, religion, sex, national origin, or age. Limit responses to 200 characters.',
    temperature: 0,
  });
  return message.content;
}

Bun.serve({
  port: process.env.PORT,
  async fetch(req: Request) {
    const { method, headers, body } = req;

    // Handle CORS preflight requests
    if (method === 'OPTIONS') {
      const res = new Response('Departed', CORS_HEADERS);
      return res;
    }
    
    if(headers.get('jlong-authorization') !== 'PersonalSiteForJordanLong') throw new Error('Unknown Authorization');
    
    //headers to handle CORS request bounces
    const responseHeaders = new Headers();
    responseHeaders.set('Access-Control-Allow-Origin', '*');
    responseHeaders.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    responseHeaders.set('Content-Type', 'application/json')
    
    if(method === 'POST' && body){
      const fullConversation = await Bun.readableStreamToJSON(body);
      const claudeAnswer = callClaude(fullConversation.conversation)
      .then((val) => {
        return new Response(JSON.stringify(val[0]), {headers: responseHeaders})
      });
      return claudeAnswer;
    }
    return new Response('Incorrect type of request', {headers: responseHeaders});      
  }
})
console.log(`listening on port ${process.env.PORT}...`);
