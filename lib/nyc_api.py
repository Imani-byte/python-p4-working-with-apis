
import requests
import json

class GetPrograms:

  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
            programs_list.append(program["agency"])

    return programs_list

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
# programs = GetPrograms().get_programs()
# print(programs)