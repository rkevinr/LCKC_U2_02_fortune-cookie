#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random


def getRandomFortune():
    fortunes = [
            'You will face a decision before starting Unit 3.',
            'If you\'re in the (U.&nbsp;S.) Mountain TZ, you\'re not in LC 101.'
            'It\'s \'hip\' to be from Square.',
            'Keeping ahead of LC 101 assignments brings peace of mind.',
            'Great LC 101 Studios work will win you a trip to Abbey Road.'
        ]
    return fortunes[random.randint(0, len(fortunes)-1)]


def gen_page_content():
    global curr_fortune

    heading = "<h1>Fortune Cookie</h1>"
    new_string_not_found = True 

    while new_string_not_found:
        fortune_string = getRandomFortune()
        if fortune_string == curr_fortune:
            continue
        else:
            new_string_not_found = False
            curr_fortune = fortune_string
            break

    fortune_line = "<p>Your fortune: <strong>" +  \
                        fortune_string + "</strong></p>"
    lucky_num_line = "<p>Your lucky number: <strong>" +  \
                        str(random.randint(1,100)) + "</strong></p>"
    refresh_button_line = '<a href="."><button>Another cookie plz!</button></a>'
    return heading + fortune_line + lucky_num_line + refresh_button_line


class MainHandler(webapp2.RequestHandler):
    def get(self):
        fc_content = gen_page_content()
        self.response.write(fc_content)


curr_fortune = ''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

