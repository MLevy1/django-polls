# django-polls

-You can't connect to github using your password.  You need a personal access token:

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

PA token is only laptop in documents folder "github inst"

-you should already be linked to the remote origin, but if not:

	git remote add origin https://github.com/MLevy1/django-polls.git

to push updated files to pythonanywhere from the remote pc:

	push files to github

		navigate to the directory
		git push --all

		if error, git pull -m "merge" then git push --all again

	pull files from github in the pythonanywhere bash terminal

		git pull
