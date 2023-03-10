from pprint import pprint

from test_task.services.cli import get_args
from test_task.company_stats import CompanyStatsFacade

from test_task.db.utils import init_db


if __name__ == "__main__":
    args = get_args()

    init_db()

    comp_stat = CompanyStatsFacade()

    comp_stat.from_spreadsheet_file(args.filename)
    comp_stat.add_to_db()

    data = comp_stat.get_total_qoil()
    data2 = comp_stat.get_total_qliq()

    pprint(data)
    print()
    pprint(data2)
