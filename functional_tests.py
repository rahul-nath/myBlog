from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()        

    def person_can_comment_and_approve_it(self):

        # Someone has heard of my blog. They go check it out.
        self.browser.get('http://localhost:8000')

        # They see the page title and header mentions my blogger name
        self.assertIn('iBlog', self.browser.title)

        # people see my home screen, which has the categories of all topics

        # on the left, they can see my more recent posts

        # if the person clicks on one of the stories, they are redirected to it

        # below the story, they can comment, but they have to fill out an "I am not a robot thing"

        # either have to sign in via facebook or the post has to be approved by me

        # allow the post automatically if it does not contain a selection of different swears and/or racist shit

        # use nltk to parse the comment for sentiment and diction. if unsatisfied, don't allow to post

        # else, the post immediately shows up

if __name__ == "__main__":
    unittest.main(warnings='ignore')


