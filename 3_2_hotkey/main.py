import traceback

from main_controller.main_controller import MainController


def main():
    try:
        main_controller = MainController()
        main_controller.start()
        
    except Exception as e: 
        traceback.print_exc()

if __name__ == "__main__":
    main()