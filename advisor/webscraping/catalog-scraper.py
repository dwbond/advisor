#!/usr/bin/python

from bs4 import BeautifulSoup

# test cases

# courseParser
# any element is wrong or missing

# programParser
# regex all the things


# PROGRAMS
def allProgramUrls(url):
  """scrape list of all program urls
  """

def programScraper(url):
  """open each url, and scrape the program requirements
  """
  programList = BeautifulSoup(open(url))

def programParser(program):
  """parsing this is going to be weird
  """

# COURSES
def courseScraper(url):
  """scrape all courses
  """
  courseList = BeautifulSoup(open(url))

  # this is actually going to be a bit different, because I'm going to
  # change the url for each iteration

def courseParser(course):
  """Return list of course elements
  """
  # Course Title
  # Credits and retakes
  # Description
  # Prerequisites
  # Corequisites
  # Lecture hours per week
  # Lab hours per week
  # Schedule of classes url

def main(courseUrl, programUrl):
  course(courseUrl)
  program(programUrl)

main("http://catalog.gmu.edu/content.php?catoid=22&navoid=4546",
  "http://catalog.gmu.edu/content.php?catoid=22&navoid=4550&expand=1&cpage=2")
