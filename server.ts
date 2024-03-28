import Anthropic from '@anthropic-ai/sdk';
import { type MessageParam } from '@anthropic-ai/sdk/resources/messages.mjs';
import express, { type Request, type Response } from "express";
import cors from 'cors';

const app = express();
//handle CORS preflight issues
app.use(cors({ origin: '*', credentials: true }));
app.use((req: Request, res: Response, next: any) => {
  if ('OPTIONS' === req.method) {
    res.sendStatus(200);
  } else {
    next();
  }
});
//parses body when post is received
app.use(express.json());

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

app.post('/', async (req: Request, res: Response) => {
  const { method, headers } = req;
  const { conversation } = req.body;
  if(headers['jlong-authorization'] !== 'PersonalSiteForJordanLong') throw new Error('Unknown Authorization');
  if(method === 'POST' && conversation){
    return res.status(200).json(await callClaude(conversation));
  }
  return res.send('Incorrect type of request');
})

app.listen(process.env.PORT, () => {
  console.log(`listening on port ${process.env.PORT}...`);
})
