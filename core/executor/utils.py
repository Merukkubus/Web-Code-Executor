import subprocess

def execute_code(language, code):
    try:
        if language == "python":
            # Выполнение Python-кода
            result = subprocess.run(
                ["python", "-c", code],
                capture_output=True,
                text=True,
                timeout=5
            )
        elif language == "javascript":
            # Выполнение JavaScript-кода
            result = subprocess.run(
                [r"C:\Program Files\nodejs\node.exe", "-e", code],
                capture_output=True,
                text=True,
                timeout=5
            )
        else:
            return {"error": f"Unsupported language: {language}"}

        # Возврат результата выполнения
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

    except FileNotFoundError as e:
        # Если интерпретатор не найден
        return {"error": f"Interpreter not found for {language}: {str(e)}"}
    except subprocess.TimeoutExpired:
        # Если выполнение кода превысило лимит времени
        return {"error": f"Code execution for {language} timed out"}
    except Exception as e:
        # Общие исключения
        return {"error": f"Unexpected error: {str(e)}"}