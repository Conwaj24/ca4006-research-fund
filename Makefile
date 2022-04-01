run: help test

data/fa_balance:
	mkdir -p data
	echo 1000000 > $@

fund_pipe:
	mkfifo $@

help:
	cat how_to_use.txt

test: fund_pipe data/fa_balance
	mkdir -p data/groups
	tail -f fund_pipe | python3 fundingAgency.py

.PHONY: test help run
