# Zavadanak

A simple python script to crawl pages recursively using headless chrome
and list some information like Time to first byte, dom load and page load


## Prerequisities

    apt-get install chromium-chromedriver

Make sure that you set 'chromeDriverPath' variable

## Usage

python zavadanak.py http://[YOUR_URL]

<pre>
                                 `` `                                            
                             `.-....-.``                                         
                           `:/++o++//::-``
                          `-//+ooosso++/-`                                                   `---::/
                          `-+ooooo+/oo+o/`                                            `.-:/ossssoooo
                          -:+++oo++//o++/.                                       .-/osyhhyyssso+/-..
                          ./+osso+++:oso/.                               ``.---/oyddddhhyyyyso+.
                          `:/os+///+::/o/-                           `-/oys++++osyyhddoooosssyys/`
                           `/+++oosso/+/:.```       `         `.//+oshhhhsooooosyssoo+:--:/++oyys+-
                        .///:::/++++//:---+/////+oosso+/:::/syyyysyhddhdy/ssoosyyyyyyyo. `.-:osys/.
                     `-osss+///:::/::--:/ssoysyyyhyhhyyssyhdyhhyyhhdddhh+/yysso+oo++++-`    .sss+-`
                 `:/oossyyyysoosoo+++oyhysssyyyhhyhhyyyyyhdhdhyhhhddhdhy/:ysooyhyyy`       `+ss+-:.:
               `/ssyyyyyyyhhyyhhhhhhhhhhhsyyhyhhhyhyyyyyhhhhhyyyhhhhhhhy/-/shddhyy-        .oso:/-//
              `syyyyyyyyyyyhhyhhhhhhhhhhhsyyhhhdhhyyyyyyyyyyyyyyyyyhyhyho-/yddhyy:          `-++- ..
             `oyhhhhhhhhhhhhhhhhhhhhhyhhhyhhhhhhdhsyyyssoosssssssyyyyyyhyo:/yyss:              `
             /yyhhhhhhhhhhhhhhhhhhhhhyhhhyhhhhhydhsyyys/--......--::::--..-:+/-`
            `yyyhhhhhhhhhhhhhhhhhhhddhhhhhhhhhhyhhoyos:           
            /yyyhhhhhhhhhhhhhhhhhdhhdhhhhhhhhhhshh+so/            
           `syysyyhyhhhhhhhhhhhhhhhhhhhhhhhhhhhsyh+o+.            
           :yyysyyysyhhhhhhddhhhhhhhhhhhhhhhhhyyyh+o/              
           oyyssyysosyyhhhhhhhhhhhhhhhhhhhyhhhyyyh++-             
          `sysssyssosssyyhhhhhhhhyhhhhhhhhhhhyssyh+/.             
          /ssssssssoosssyyyhhhhhhhyhhhhhhhhhyyssyh//`              
          +ssssssoo//ssssyyyhhhhhhhhhhhhhhhyyssoyd/+`
</pre>

# Troubleshoot

If you get such error make sure that you are not running the app as root

    selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally.
      (unknown error: DevToolsActivePort file doesn't exist)
