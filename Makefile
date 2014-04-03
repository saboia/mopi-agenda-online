help:
	@echo 'USAGE: make <target>'
	@echo '-----------------'
	@echo 'Available targets'
	@echo '-----------------'
	@echo '    clean..........................removes all .pyc files and all reports'
	@echo '    splinter.......................runs all splinter cartola tests'


clean:
	@echo "Cleaning up build, *.pyc and *.min.* files..."
	@find . -name '*.pyc' -exec rm -rf {} \;

splinter: clean selenium_up
	@echo "Running splinter tests..."
	@nosetests -s -x --verbose test_splinter/*$(file)*
	@make selenium_down
	@echo "DONE"


selenium_up: selenium_down
	@echo "Running selenium server..."
	@java -jar data/selenium-server/selenium-server.jar > /dev/null 2>&1 &

selenium_down:
	@echo "Killing selenium server..."
#	@-ps aux | egrep 'selenium.server' | egrep '.jar' | egrep -v grep | awk '{ print $$2 }' | xargs kill -9
	@-ps aux | grep 'selenium.server' | grep -v grep | tr -s ' ' | cut -f 2 -d ' ' | xargs -n1 kill -9
