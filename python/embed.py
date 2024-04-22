import voyageai
from pinecone import Pinecone

pc = Pinecone(api_key="9106eb0c-30db-4c62-b6f2-68155e21dc90")
# .init(api_key="9106eb0c-30db-4c62-b6f2-68155e21dc90")
index = pc.Index("personal-site-data")

vo = voyageai.Client(api_key="pa-gd-AL9ce-gonQWb2EalolEAKRhW78_VBejhE8DHupSg")
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")
everest_experience_raw = "<description>Deployed a custom trained Large Language Model on Google Cloud’s Vertex AI to extract pertinent data from over 10k unstructured emails per day, increasing parsed emails for customers by 200% with a sub 3 second latency.</description><description>Created 15k lines of training data using Python to simplify prompt engineering of our custom LLM. This reduced necessary context tokens per request from over 1500 to 70.</description><description>Led Everest Drivers App development and deployment on iOS and Android using React Native, TypeScript, and Google Cloud’s Firebase leading to better product penetration for 20% of companywide book of business.</description><description>Orchestrated integration of Driver App with backend using Node.js, Express.js and AWS DynamoDB. Engineered API endpoints for authentication, dynamic session management, user event data transmission, and core functionalities.</description><description>Utilized Terraform to deploy and maintain NoSQL tables on DynamoDB, optimizing backend for fundamental app features. Stored user usage events, contributing to Everest's data lake for improved AI pricing recommendations.</description><description>Implemented Storybook, Jest, and Cypress testing libraries for comprehensive component, unit, and end-to-end testing reducing code review comments by 30%. </description><description>Maintained AWS Elastic Compute Cloud and Elastic Beanstalk deployments for Everest's web applications, ensuring seamless operation and a reliable user experience through >98% uptime.</description><description>Developed plugins for major email clients (Outlook, Gmail, Front), reducing both user clicks and open applications. Simplified RFP responses from 100-200 clicks to 3 and open applications from 4 to 1.</description><description>Operated within an agile framework by organizing tasks on Jira's sprint board. Provided clear visibility into biweekly objectives, story point values, and specific due dates for efficient project management. </description>"
everest_experience = everest_experience_raw.replace("<description>", 'Work Experience with Everest AI: ').split("</description>")
nautilus_experience_raw ="<description>Built a tri-purpose Docker Compose, Docker Swarm and Kubernetes deployment tool and visualizer by expanding its legacy Docker-specific yaml parser to create a streamlined container service agnostic deployment visualization tool.</description><description>Retrofitted Redux Toolkits into application by mapping stateful functionality and rewriting functions as reducer slices to update legacy state management to install a single source of truth and to avoid prop drilling enabling better scalability, clearer and easier refactoring, and offer access to Redux Developer Tools in the browser.</description><description>Refactored React Hooks into legacy codebase by migrating class components to functional components, writing in various Hooks and removing classic lifecycle methods to improve testing, readability and organization of code.</description><description>Used the Electron framework to build a multi-platform desktop application which allows for one front-end code base improving application scalability and maintainability.</description>"
nautilus_experience = nautilus_experience_raw.replace("<description>", 'Open Source Work Experience with Nautilus: ').split("</description>")
uchs_experience_raw ="<description> Tailored math instruction to meet the unique needs of students with diverse learning disabilities, including ADHD, dyslexia, and autism spectrum disorders.</description><description>Conducted individualized education plans (IEPs) and modified curriculum materials to provide accessible and inclusive learning experiences, resulting in significant academic progress among students.</description><description>Participated in regular IEP meetings with parents and caregivers, ensuring effective communication and a cohesive support system for students with special needs in the math curriculum.</description>"
uchs_experience = uchs_experience_raw.replace("<description>", 'Work Experience with Uncommon Charter High School: ').split("</description>")
americorps_experience_raw = "<description> Led, trained, and lived with a volunteer team of 6-9 Corps Members to volunteer for non-profits, government organizations and faith-based organizations collectively volunteering over 12,000 hours.</description><description>Managed a $31,000 cumulative budget to feed and sustain Corps Members throughout collective ten months of service and to house the team during 20 nights of work-related travel.</description><description>Built relationships with project sponsors to create a harmonious work environment where across various projects our team repaired five homes, supported the vaccination of over 45,000 New Jersians with FEMA and New Jersey local governments, served over 2700 meals with food banks, and beautified an 80 acre camp for people with disabilities</description>"
americorps_experience = americorps_experience_raw.replace("<description>", 'Volunteer Work Experience with AmeriCorps NCCC: ').split("</description>")
uhc_experience_raw = "<description> Managed and maintained relationships for a book of business of over 75 Key Account employer groups amounting to over $150 million in annual healthcare spend and was responsible for servicing and renewing over 20,000 members.</description><description>Led over 75 open enrollment meetings in 2015 to teach organization's employees how UnitedHealthcare’s plans worked and outlined the nuances and features of their plan so members could easily obtain insurance benefits.</description><description>Designed and organized over 30 wellness plans for employers by setting up on-site events like biometric screenings, organizational trainings and sessions to increase employee satisfaction and decrease absenteeism.</description><description>Effectively leveraged client and broker relationships to renew over 89% of membership in 2015 counting for 117% to book of business persistency membership goals and ranked top 15% within the organizational nationally.</description><description>Developed and presented reporting on claims and utilization for an organization’s health insurance plan and offered solutions using UnitedHealthcare’s products for clients who had between $5 and $100 million in annual healthcare spend.</description><description>Created operational efficiencies so the account managers could effectively renew business across the state to renew over 110% of total membership goals.</description>"
uhc_experience = uhc_experience_raw.replace("<description>", 'Work Experience with UnitedHealthcare: ').split("</description>")
high_level_hobbies = ["Jordan has many hobbies including cooking and baking, hiking and camping, travelling, and playing some video games"]
work_related_experiences = [
  "Jordan built this personal website by: using Bun, Vite, and Vercel to quickly deploy a functional frontend web application",
  "Jordan built this personal website by: hosting his backend as an Amazon Web Services Lambda Function, he chose to go serverless because it was a very inexpensive option to host his backend api. He's aware of the cold start latency but this remedied by Jordan making a silent call on initial page load to open the lambda function before the user asks their first question. Lambda functions stay open ~15 minuutes with use so keeps latency and costs to a minimum",
  "Jordan built this personal website's AI by: using Anthropic's SDK to access Claude's Opus model, it's highest quality LLM. He then used Voyage AI's embedding model and Pinecone to create a RAG architecture to retrieve and only respond with data about him",
  "At Everest AI, Jordan researched, chose, trained/fine-tuned, prompt engineered and deployed a Generative AI into an existing application. He needed to train the LLM because prompt engineering alone wasn't yielding outputs in a format that they could work with (JSON). To do this training, Jordan created thousands of lines of synthetic data using python scripts",
  "At Everest AI, Jordan led the development and deployment of their mobile app, the Everest Driver's App using React Native to Apple's iOS and Android's Play Store.", 
  "At Everest AI, for the mobile app, He also created api endpoints to tie into Everest's existing applications and infrastructure. The api endpoints were built in Node.js, using the Express.js framework and written in TypeScript.",
  "At Everest AI, Jordan built api endpoints to optimize an existing workflow for a new product. This new product required making bulk calls and the existing workflow wasn't built to accomodate the sort of volume needed to meet the minimum viable product of this new feature. Jordan's optimized endpoints allowed an increase of around 500 times what was previously acceptable based on the previous workflow"
]
food_related_hobbies = [
  "One of Jordan's food related hobbies and facts: if he feels like he buys out certain foods often, he'll eventually attempt to make it figuring he can do it cheaper and better",
  "One of Jordan's food related hobbies and facts: since road tripping through Scotland in 2022, he likes baking shortbread cookies",
  "One of Jordan's food related hobbies and facts: he bakes neopolitan style pizzas using a homemade sourdough crust, his favorite which some have praised as the best pizza they've ever had is his carbonara pizza which has bacon, eggs, mozzarella cheese, and a citrus habanero olive oil",
  "One of Jordan's food related hobbies and facts: he's an avid smoothie drinker, making an orange smoothie daily for breakfast which includes mandarins (because they're easier to peel than navels), frozen ginger, frozen pineapple, carrots, homemade kombucha and a few dashes of cinnamon",
  "One of Jordan's food related hobbies and facts: he's an excellent grill master because he knows the right way of cooking most meat over a fire so it's juicy and flavorfull",
  "One of Jordan's food related hobbies and facts: he's made several phenomenal cheesecakes. They're good because the lemon zest adds a subtle citrus flavor while otherwise being creamy, appropriately dense, and beautiful",
  "One of Jordan's food related hobbies and facts: he's been making homemade kombucha for several years now, maintaining roughly the same SCOBY since starting, his favorite is a passionfruit flavored kombucha because it's tart, fruity, and mildly sweet",
  "One of Jordan's food related hobbies and facts: he doesn't drink much alcohol, he prefers making a sugar-lite mocktail. He doesn't like how many mocktails these days are very sugary or too close to juice, he gets recipes from a great book he can recommend to you!",
  "One of Jordan's food related hobbies and facts: his favorite dishes to eat out are birria style mexican food, thai curries, szechaun style chinese, sushi, and baked desserts like carrot cake and cookies from Levain Bakery"
]
outdoors_sports_hobbies = [
  "One of Jordan's sports related hobbies: he shoots recurve archery. There are a couple ranges in Brooklyn where you can shoot arrows safely indoors to practice at regulation distance",
  "One of Jordan's outdoor related hobbies: he loves hiking. His particularly enjoys fall, spring and winter hikes, he typically avoids the summer because it's too hot. His favorite places to hike include the Pennsylvania Grand Canyon area, Sequoia National Park and Yosemite National Park",
  "One of Jordan's outdoor related hobbies: his favorite place that he's camped is Cherry Springs State Park, one of the darkest places by the east coast. He's camped there 4 times, including to see the Perseids Meteor Shower",
  "One of Jordan's outdoor related hobbies: his most frightening moments while hiking was when he encountered a brownish looking black bear on the Cloud's Rest hiking trail in Yosemite National Park. He's also encountered a rattlesnake in Pennsylvania",
  "One of Jordan's sports related hobbies: he doesn't play too many sports really, grew up with bad knees but eventually did research and learned how he can physically active without pain. His predominant sport of choice is archery although he recently starting using a Peloton.",
  "One of Jordan's sports related hobbies: his most followed sport is Formula 1 racing, he's a fan of Lewis Hamilton, Sergio Perez and Alex Albon. He got into F1 after watching the first two seasons of Drive to Survive",
  "One of Jordan's outdoor related hobbies: his most challenging camping ordeal was when he road tripped around Scotland, he wasn't aware, because Scotland doesn't readily divulge this information, that there are little bugs called Midges, similar to Canadian Black Flies which swarm and menace anyone nearby and have a nasty bite. During one night Jordan needed to move his camp after setting up to find a place with more wind where the midges were few"
]
personal_questions_avoid = [
  "Jordan cannot answer questions about: race",
  "Jordan cannot answer questions about: ethnicity",
  "Jordan cannot answer questions about: relationship status",
  "Jordan cannot answer questions about: age",
  "Jordan cannot answer questions about: national origin",
  "Jordan cannot answer questions about: religion",
  "Jordan cannot answer questions about: disability"
]
free_time = [
  "Jordan's favorite tv shows are Top Chef, The Amazing Race, Avatar: The Last Airbender, Fullmetal Alchemist, The Wire, Game of Thrones",
  "Jordan's favorite video games are the Mass Effect Trilogy including Andromeda, Baldur's Gate 3, Breath of The Wild, Tears of the Kingdom, Civilization 6, Shogun 2: Total War, Dungeons and Dragons",
  "Jordan is an avid gardener, he grows garlic, sumo orange trees, basil and san marzano tomatoes for his pizzas, and has grown arugula, lettuce, and scallions in the past",
  "While doing house chores, Jordan listens to the Economist magazine's e-reader which has professional broadcasters read each article. He's likely listened to every magazine front to back for around five years.",
  "Jordan has no pets but grew up with cats and had a dog"
]
fun_facts = [
  "A fun fact about Jordan is that: he is a twin",
  "A fun fact about Jordan is that: he shares a birthday with his namesake, Michael Jordan, the famous basketball player",
  "A fun fact about Jordan is that: has spent the night in all but six American states, Alaska, North Dakota, Maine, Vermont, Idaho, and Washington",
  "A fun fact about Jordan is that: he was a long-haul truck driver for 2.5 years",
  "The craziest thing Jordan has ever done was when he was backpacking around Europe, he was sick during his stay in London. London is home to much of his favorite music so a few weeks later when he learned that his favorite artist was playing there on his birthday, he planned to go back whereever he was on his trip. The night before his birthday he was in Barcelona where he met some people and stayed out late into his birthday morning. He woke up that afternoon, took a flight to london, danced for hours at the concert and took a 6am flight back to Barcelona where he left all his belongings."
]
pre_embedding = list(everest_experience + 
                  uchs_experience + 
                  americorps_experience +
                  uhc_experience +
                  high_level_hobbies +
                  work_related_experiences +
                  food_related_hobbies +
                  outdoors_sports_hobbies +
                  personal_questions_avoid +
                  free_time +
                  fun_facts)
result = vo.embed(pre_embedding, 
                  model="voyage-large-2",
                  input_type="document").embeddings
vectors = []
for i in range(len(result)):
  vectors.append({
    "id": f"vec{i}",
    "values": result[i],
    "metadata": {
      "originaltext": pre_embedding[i]
    }
  })
num_upserted = index.upsert(vectors=vectors)
print(num_upserted)