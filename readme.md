use cases:

day codes:: M = Monday; T = Tuesday; W = Wednesday; R = Thursday; F = Friday, S = Saturday, U = Sunday

@pt=d:t #personal
@wt=d:t #work #personal
@weekly=r:1w,MTWRFSU
&eric=eric@test.com
@mgrs=t:&eric,bob@gmail.com
@wn=@wt @mgrs

commands (always show current state):
ls @|&|#
? d:t +0,+1,-1
? #work
? @work
=@macro (changes current state)
= (changes back to default state)
def @default=... (sets default state, default is reserved)


default(s):
day start: 7am
day end: 10pm

syntax:
d=due
r=repeat (w|m|d)
t=to (persons to keep in loop)
def=define something (@|&|*|#)
  @=macro
  &=contact (email)
  #=context

relative dates:
in x h|hr|hrs|hour|hours|m|min|mins|minute|minutes|day|days|d|m/d|m/d/y|m|t|w|r|f|s|u
x h|hr|hrs|hour|hours|m|min|mins|minute|minutes|day|days|d|m/d|m/d/y|m|t|w|r|f|s|u ago
+ (default day)
- (default day)
today|t
yesterday|y
tomorrow|+

@default=#personal d:t,2pm
=d:t,3pm
(state changed)

=
(back to default)

@personal=#personal d:+,4pm
=@personal

&bob=bob@test.com

submit status report to bob tomorrow at 2pm
submit status report to bob today at 2pm
submit status report to bob 2pm
submit status report to bob tomorrow
submit status report to bob in 30m
submit status report in 25 mins
submit status report to bob

&mark=mark@deployfx.com

pay back mark $35 (for shoes yesterday)
pay back mark $35
owe mark $35
collect $35 mark (for shoes tomorrow)

get parking pass 30m
get parking pass +30m
get parking pass 2pm tomorrow
get parking pass +1,2pm
get parking pass 2pm +1
get parking pass 2pm +
get parking pass +t
get parking pass t
get parking pass d:t

=d:30m
get parking pass
get parking pass t:mark,bob

get time off for appointments d:+
