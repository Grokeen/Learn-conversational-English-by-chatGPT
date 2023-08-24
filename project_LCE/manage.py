#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_LCE.settings')
    try:
        # Djanngo 관리 모듈 import
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 관리 모듈 오류 시, ImportError에 등록된 명령어 실행
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
