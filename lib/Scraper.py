import requests
from bs4 import BeautifulSoup  # Ensure this import is included
from Course import Course  # Ensure this import is correct

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        """Fetches and returns the parsed HTML document from the web page."""
        response = requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses")
        doc = BeautifulSoup(response.text, 'html.parser')
        return doc

    def get_courses(self):
        """Returns the list of course elements from the page."""
        return self.get_page().select('.post')

    def make_courses(self):
        """Creates Course objects from the scraped data and populates self.courses."""
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        """Prints the course details."""
        self.make_courses()  # Ensure courses are populated before printing
        for course in self.courses:
            print(course)

# Example of how to use the Scraper
if __name__ == "__main__":
    scraper = Scraper()
    scraper.print_courses()  # This will print the list of courses
