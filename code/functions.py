from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_and_save(url, output_path):
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Open the website
    driver.get(url)

    # Set a timeout for waiting (e.g., 10 seconds)
    timeout = 10

    try:
        # Wait until the cookie acceptance button is present
        cookie_button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.mb-2"))
        )
        # Adjust the scroll to center the cookie button in view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", cookie_button)
        cookie_button.click()

        # Wait for a brief moment to allow page adjustment
        WebDriverWait(driver, timeout).until(EC.staleness_of(cookie_button))

        # Wait until the 'Toon meer details' button is present
        details_button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.d-inline.ng-star-inserted"))
        )
        # Adjust the scroll to center the 'Toon meer details' button in view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", details_button)
        details_button.click()

    except Exception as e:
        print("Error: ", e)
        driver.quit()
        return

    # Extract the page source
    html = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Extract and print text
    page_text = soup.get_text()

    # Write the text to a file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(page_text)

    # Close the driver
    driver.quit()

# Example usage of the function
scrape_and_save('https://www.biddit.be/nl/catalog/detail/252452', 'output_file.txt')
