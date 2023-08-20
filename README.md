# sql-alchemy-intro-blogly-part1
http://curric.rithmschool.com/springboard/exercises/flask-blogly/

Fixed previous error. Now get the error: 
======================================================================
FAIL: test_add_user (tests.test-routes.TestRoutes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/shangita/Desktop/UMASS_Global/Assessment/sql-alchemy/sql-alchemy-intro/sql-alchemy-intro-blogly-part1/tests/test-routes.py", line 52, in test_add_user
    self.assertEqual(response.status_code, 302)
AssertionError: 200 != 302

----------------------------------------------------------------------
Ran 5 tests in 0.175s

FAILED (failures=1)


Research:
The error you're encountering (AssertionError: 200 != 302) indicates that the expected status code for the response is 302 (which stands for a redirect), but the actual status code received is 200 (which stands for a successful response). This likely means that the redirect after adding a new user is not working as expected.

It's possible that there's an issue with the way the redirect is being handled in your route. To troubleshoot this issue, consider the following steps:

Check Your Redirect Code: Make sure the redirect('/users') code in your users_new route is correct. Double-check that there are no typos or mistakes in the URL.

Inspect Response Content: Sometimes, if there's a validation error or some other issue, your application might not redirect. As a result, the test case could receive a normal 200 response instead of the expected redirect. You can print out the content of the response to see what's being returned. Add the following line at the end of your test_add_user test case:

python
Copy code
print(response.data)
This will print out the content of the response, which might give you more insight into what's happening.

Check Your Application Logs: Check the logs of your Flask application for any error messages or warnings related to the redirect. This might give you more information about why the redirect is not happening.

Inspect the Redirect in a Browser: Manually perform the action that the test is supposed to simulate (adding a new user) in a web browser and see if the redirect works as expected. This can help you confirm if the issue is specific to the test or if it's a broader problem in your application.

Update Your Test Logic: If you're certain that the redirect is working as expected when manually testing in a browser, you might need to adjust your test logic. Sometimes, tests can be sensitive to timing or small differences. Ensure that your test setup accurately simulates the behavior of a user adding a new user and being redirected.

Check for Any Other Redirects: Make sure that there are no other redirects happening before the /users redirect. If there's another redirect before that, it might interfere with your test expectations.

Review Flask Debug Toolbar: If you're using Flask Debug Toolbar, it might also affect the behavior of your application. Temporarily disable it and see if the issue persists.

By following these steps, you should be able to narrow down the issue and identify what's preventing the redirect from working as expected in your test case.
