from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


timeout = 8


class Navegador:
    
    def  __init__(self, headless = False):
        self.options = Options()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-user-media-security=true")
        self.options.add_argument("--use-fake-ui-for-media-stream")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-application-cache")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_extension('utils/instanciadorSelenium/autoSolverHCaptcha.zip')
        
        if headless == True:
            self.options.add_argument("--headless")
        
        #Inicia o Navegador
        chrome_service = ChromeService(ChromeDriverManager().install())
        
        self.driver = webdriver.Chrome( service=chrome_service, options=self.options )
        
        
        stealth(
            self.driver,
            languages = ["pt-BR", "pt"],
            vendor = "Google Inc.",
            platform = "Win32",
            webgl_vendor = "Intel Inc.",
            renderer= "Intel Iris OpenGL Engine",
            fix_hairline = False,
            run_on_insecure_origins = False,
        )
        
        self.driver.implicitly_wait(timeout)
        
        
        
def Abrir_navegador():
    navegador = Navegador()
    return navegador.driver