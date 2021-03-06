"""Entry point for cli orgatization command."""

from findzen.commands.command_plus_docs import CommandPlusDocs
from findzen.models.org import Organization
from findzen.pretty_print import pretty_print_orgs
from findzen.utils import search_cache, sanitize_argument
import logging
import sys

logger = logging.getLogger('findzen')


class OrgCmd(CommandPlusDocs):
    """Search for organization by a given field. Returns the organization details, plus it's users and tickets."""
    name = 'organization'

    def _init_arguments(self) -> None:
        for field in Organization.__fields__:
            self.add_argument(
                f'--{field}',
                help=f'search for organization with {field} field')

    def _run(self, args) -> int:
        try:
            if len(sys.argv) != 4:
                raise BaseException(
                    "Wrong arguments: Requires exactly 1 field key and value to search with. Empty values are indicated by ''. ")

            search_by_field = sys.argv[2][2:]
            search_by_value = sanitize_argument(sys.argv[3])
            
            orgs = self._search_org(search_by_field, search_by_value)

            if len(orgs) == 0:
                print(
                    f'Organization with {search_by_field} {search_by_value} not found.'
                )
                return 0

            pretty_print_orgs(orgs)

        except BaseException as err:
            logger.error(f'Failed: {err}')
            return 1

        return 0

    def _search_org(self, search_by_field: str, search_by_value: str) -> list:
        """Given a field and value, search for orgs. Returns list of matching orgs."""
        if search_by_field not in Organization.__fields__:
            raise BaseException(
                'Wrong arguments: Provided field name is not a field in Organizations data.'
            )

        if search_by_field == 'id':
            org_ids = [search_by_value]
        else:
            org_ids = search_cache('organization', search_by_field,
                                    [search_by_value])

        orgs = search_cache('organization', 'id', org_ids)

        return orgs
