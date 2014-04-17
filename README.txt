1
==
-Run using Pageranks.jar to get pageranks in binary format.
java -jar Pageranks.jar <graph-file> <no-of-shards> edgelist

#no-of-shards will be around 1 for each 20-50 million edges. use value of around 75 for our dataset.

or if you want to run through .cpp file use the command:

./pagerank bin/example_apps_pagerank file <graph-file>

and give edgelist as parameter after pressing enter.





2
==
-Extract the pageranks in readable format using ReadablePageRanks.jar , redirect th eoutput to pageranks file.

java -jar ReadablePageRanks.jar <pageranks-binary-file-path> >pageranks

#pageranks-binary-file would be .vout file.
#pageranks file would be a file containing each user's pagerank with each line corresponding to its user id.



3
==
Now get sortedpageranks file by running ExternalMergeSort file.

java ExternalMergeSort <pageranks-file-folder-path>

//provide the path of folder in which pageranks file is present.
//the sorted file would be present in temp folder in the folder specified in args[0].

From this file you need to extract Top K users to crawl theri tweets.We have chosen K as 50 here

head -50 sorted-pageranks-file > users.txt




4
==

python 	seleniumfortweetstatuscrawling.py <user-id>

use python code to extract tweets of each userid from the users.txt file in their separate file.




5
==
-->store all the 50 users file inside mallet in a folder "Tweets" and the run the following commands to generate the training model.


1)This command imports the Tweets directory content:

	bin/mallet import-dir --input Tweets/ --keep-sequence --remove-stopwords --output Train.mallet



2)This command generates the topic model "doc-topics.txt" and topics mapping file "topic-keys.txt":

	bin/mallet train-topics --input  Train.mallet --num-topics 20  --num-iterations  1000 --inferencer-filename inferencer --output-topic-keys topic-keys.txt  --output-doc-topics  doc-topics.txt

we have chosen to generate 20 topics and 1000 iterations for training.



3)Now store the test users' tweets file in some folder like "test" and run upon the trained model to get his topics.


	bin/mallet import-dir --input test/ --keep-sequence --remove-stopwords --output test.mallet  --use-pipe-from Train.mallet

	bin/mallet infer-topics --input test.mallet --inferencer inferencer --output-doc-topics topics-prob.txt --num-iterations 100

topics-prob.txt gives the prob of each topics' for this user.
