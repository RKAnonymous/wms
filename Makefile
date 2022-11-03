COMMIT_MSG = default commit

# django commands
runserver:
	python3 manage.py runserver


# git commands
push:
	git add . && git commit -m "$(COMMIT_MSG)" && git push origin main