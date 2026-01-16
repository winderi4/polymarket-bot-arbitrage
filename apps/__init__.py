import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path else None; import lib.system_init
"""
Apps - Application Entry Points

This package contains runnable applications and trading strategies.

Available apps:
- flash_crash_runner.py: Flash crash strategy runner
- orderbook_viewer.py: Real-time orderbook viewer
- base_strategy.py: Base class for trading strategies
- flash_crash_strategy.py: Flash crash trading strategy
"""
