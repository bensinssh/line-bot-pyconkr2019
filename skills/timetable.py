#  Copyright 2019 LINE Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


from linebot.models import TextSendMessage

from skills import add_skill


@add_skill(r'시간표', help_text='파이콘 2019 프로그램 시간표를 제공합니다.')
def get_timetable(message):
    return TextSendMessage(
        text='시간표는 https://www.pycon.kr/timetable/talks (컨퍼런스)'
             ', https://www.pycon.kr/timetable/tutorial (튜토리얼)'
             ', https://www.pycon.kr/timetable/sprint (스프린트)'
             '에서 확인해주세요'
    )
