import nltk 

from nltk.tokenize import TweetTokenizer

from nltk.corpus import stopwords
processed_word_list = []

text = "DATA ENGINEER At Wooga we work to create games that millions of players around the world enjoy. Once we launch a game that is just the beginning though, we work hard to constantly improve and optimise our games to make them even more amazing experiences. To achieve that we use a combination of creativity and data. The latter is where you come in.Our data engineers own the infrastructure that empowers our game teams to analyse and improve our games. You will work with a number of teams including data insights and various engineering teams to ensure we can collect and action the data.About the job You will develop and improve our tracking infrastructure.You will evaluate and develop Big Data solutions, see if they can be beneficial for us (e.g. Apache Spark or Flink).You will help our game teams to track the data they need to evaluate new features and improve our games.You will improve our in-house A/B-test solution.You will support our team of data scientists. You will provide the infrastructure to make them as productive as possible.You will ensure data consistency and quality. This means you understand exactly how our data pipeline looks like. You will make sure and help the game teams to stay consistent with it.You will operate our data infrastructure. We are strong believers in a “DevOps” setup, meaning there is no separation of development and operations. You will build an infrastructure that does not fail, but if it fails you will be able to fix it.You have a degree in Computer Science and be ready to apply this in a dynamic working environment.You want to build a stable and scalable Business Intelligence infrastructure processing tons of data every day.You know that KAFKA is not just an author.You love data. You love to dig into stuff, and work on a problem until it is solved.You are smart and have a “getting things done” mentality.You are highly motivated and a quick learner.You have heard of, and ideally have used, one or more of the programming languages we use: Ruby, Ruby on Rails, Scala, Java, Python, Lua, or SQL.Why join usA fast paced job. New challenges all the timeDeep insight into the start-up, internet and mobile gaming environment and an excellent start for your careerHelping to build a next generation Business Intelligence solution, in a market that is spearheading the development in this area"

tknzr = TweetTokenizer()

for w in tknzr.tokenize(text):
	if w not in stopwords.words('english'):
		processed_word_list.append(w)

print(processed_word_list)
