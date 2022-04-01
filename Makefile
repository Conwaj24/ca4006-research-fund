run:
	./start.sh
fund_pipe:
	mkfifo $@

test: fund_pipe
	tail -f fund_pipe | python funding_agency.py

.PHONY: test
