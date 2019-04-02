package SeleniumReadSentences;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.HashMap;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class FinalYearProject {
	public static void main(String[] args) throws InterruptedException, FileNotFoundException {
		//Firefox System.setProperty("webdriver.gecko.driver", "C:\\Users\\I342039\\Desktop\\Selenium\\geckodriver.exe"); 
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\I342039\\Desktop\\Selenium\\chromedriver.exe"); 
		HashMap<String, Object> prefs = new HashMap<String, Object>();
		prefs.put("profile.default_content_setting_values.notifications", 2);
		ChromeOptions options = new ChromeOptions();
		options.setExperimentalOption("prefs", prefs);
		WebDriver driver = new ChromeDriver(options);
		WebDriverWait wait = new WebDriverWait(driver, 20);
		PrintWriter pw = new PrintWriter(new File("FYPNonHateSpeech2.csv"));
        StringBuilder sb = new StringBuilder();
        driver.get("https://randomwordgenerator.com/sentence.php");
		driver.manage().window().maximize(); 
		for(int count = 0; count < 10000; count++) {
			
			 
			wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"options\"]/table/tbody/tr[2]/td/input[2]")));
			WebElement element = driver.findElement(By.xpath("//*[@id=\"options\"]/table/tbody/tr[2]/td/input[2]"));
			element.click();
		
			wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"result\"]/li/div/span")));
			element = driver.findElement(By.xpath("//*[@id=\"result\"]/li/div/span"));
			String string = element.getText();
			System.out.println(count + " " + string);
			
	        sb.append(string);
	        sb.append('\n');
		}
		
		pw.write(sb.toString());
        pw.close();
	}
}
