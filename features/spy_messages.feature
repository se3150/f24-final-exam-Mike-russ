Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    when I set Encode to the inputfield decoder-setting
    and I set 3 to the inputfield shift-amount
    and I set Secret Message To Decode to the inputfield letters
    then I expect that decoded_message contains the text Vhfuhw Phvvdjh Wr Ghfrgh

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    when I set Decode to the inputfield decoder-setting
    and I set 3 to the inputfield shift-amount
    and I set Vhfuhw Phvvdjh Wr Ghfrgh to the inputfield letters
    then I expect that decoded_message contains the text Secret Message To Decode
