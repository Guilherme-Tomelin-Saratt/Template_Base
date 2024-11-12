from src.services.automation_service import AutomationService
from src.helpers.utilities import instantitate_logs

logger = instantitate_logs()

def main():
   try:
      automation = AutomationService()
      automation.execute()
   except Exception as e:
      logger.error(e)
if __name__ == "__main__":
    main()