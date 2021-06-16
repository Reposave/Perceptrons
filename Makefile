install: venv 
		. venv/bin/activate; pip3 install -Ur requirements.txt
venv :
	test -d venv || python3 -m venv venv
 
clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	rm -rf __pycache__
 
run:
	@python3 ValueIteration.py 3 2 -start 0 0 -end 2 0 -k 3

run_test:

run1:

run_c:
	
run_c2:
	
runq:

runq2:

runq3:

runb:
	
example:
	@python3 Example.py
	
	#source ./venv/bin/activate
