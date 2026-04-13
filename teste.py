from datetime import datetime
date = datetime.now()
print(datetime.now().strftime("%d%m%Y%H%M%S"))
"""
%d/%m/%Y → 13/04/2026
  · %Y-%m-%d → 2026-04-13
"""