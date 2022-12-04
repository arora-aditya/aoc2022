RED=\033[0;31m
GREEN=\033[0;32m
BLUE=\033[36m
NC=\033[0m

day    := $(shell date +%-d)
filetd := day$(day).py
comment:= ""

run: ## Run solution for day=X (default based on day of month)
	python3 ${filetd}

input: ## Get input for day=X (default based on day of month)
	@python3 helper/getInput.py ${day}
	@git add .
	@code day${day}.py inputs/input${day}.txt ..
	@echo "${GREEN}input stored in input${day}.txt${NC}"

README: ## Update root README
	@python3 helper/generateREADME.py ${day}
	@git add .
	@echo "${GREEN}README generated${NC}"

DONE: README ## update README and push up to git
	@cd ~/github/aoc2022
	@git add .
	@git commit -am "day ${day} ✅" -m "${comment}"
	@git push
	@echo "${GREEN}pushed to git${NC}"

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "${BLUE}%-20s${NC} %s\n", $$1, $$2}'