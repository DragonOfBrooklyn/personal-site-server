import Anthropic from '@anthropic-ai/sdk';
import { type MessageParam } from '@anthropic-ai/sdk/resources/messages.mjs';

const PORT = 3000;
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
  console.log('conversation from frontend', convo);
  const message = await anthropic.messages.create({
    max_tokens: 100,
    messages: convo,
    model: 'claude-3-opus-20240229',
    system: 'You should only respond with known information about Jordan Long. Restrict information that cannot be legally asked during an interview such as race, color, religion, sex, national origin, or age. Limit responses to 200 characters.',
    temperature: 0,
  });
  return message.content;
}

Bun.serve({
  port: PORT,
  async fetch(req: Request) {
    const { method, headers, body } = req;
    // Handle CORS preflight requests
    if (method === 'OPTIONS') {
      const res = new Response('Departed', CORS_HEADERS);
      return res;
    }
    
    if(headers.get('jlong-authorization') !== 'PersonalSiteForJordanLong') throw new Error('Unknown Authorization');
    const responseHeaders = new Headers();
    responseHeaders.set('Access-Control-Allow-Origin', '*');
    responseHeaders.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    if(method === 'POST' && body){
      const reqBody = await Bun.readableStreamToJSON(body);
      let claudeResponse;
      callClaude(reqBody)
        .then((value): void => {
          console.log('claude response in then... ',value);
          claudeResponse = value;
        })
      // console.log('response from claude ',claudeResponse);
      // if(Promise.)

      const res = new Response(await claudeResponse, {headers: responseHeaders});
      console.log('sending back to frontend', claudeResponse);
      return res;
    }

    //Handle CORS request bounces
    const res = new Response('Hello Bun!!!', {headers: responseHeaders});
    return res;
      
  }
})

console.log(`listening on port ${PORT}...`);