#!/bin/bash

for file in `ls clustertest*` 
do
	train=`echo $file | sed s/test/train/`
	pwd=`pwd`
	pushd /home/amber/Code/IllinoisNerExtended-v2.1
	trainInfo=`echo $file | sed s/test/trainInfo/`
	testResults=`echo $file | sed s/test/output/`
	config=`echo $file | sed s/clustertest/config.cluster/`
	time java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -train $pwd/$train -test $pwd/$file -c true DemoConfig/$config &> $pwd/$trainInfo
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -test $pwd/$file -c true DemoConfig/$config &> $pwd/$testResults
	lbjResults=`echo $file | sed s/test/lbj/`
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -test $pwd/$file -c true DemoConfig/ner.conll.config &> $pwd/$lbjResults
	popd
done
