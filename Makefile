
#pip_options = --no-deps

help:
	@echo 'USAGE: make <target>'
	@echo '-----------------'
	@echo 'Available targets'
	@echo '-----------------'
	@echo '    clean..........................removes all .pyc files and all reports'
	@echo '    splinter.......................runs all splinter  tests'



setup:
	@echo "Instalando as dependencias para o ambiente local..."
	@echo "Installing Python Libraries ..."
	@pip install $(pip_options) -r requirements.txt
	@echo "\n======> DONE - All libs are Installed! <======\n"

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
