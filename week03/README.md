<table class="cs_container"><tbody><tr>
    <!-- ngRepeat: col in cheatsheets --><td ng-repeat="col in cheatsheets" class="bigrow ng-scope">
      <!-- ngRepeat: cs in col --><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Basics</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">.</td><td class="ng-binding">Any character except newline</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">a</td><td class="ng-binding">The character a</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">ab</td><td class="ng-binding">The string ab</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">a|b</td><td class="ng-binding">a or b</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">a*</td><td class="ng-binding">0 or more a's</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\</td><td class="ng-binding">Escapes a special character</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Quantifiers</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">*</td><td class="ng-binding">0 or more</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">+</td><td class="ng-binding">1 or more</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">?</td><td class="ng-binding">0 or 1</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">{2}</td><td class="ng-binding">Exactly 2</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">{2, 5}</td><td class="ng-binding">Between 2 and 5</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">{2,}</td><td class="ng-binding">2 or more</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(,5}</td><td class="ng-binding">Up to 5</td></tr>
        
        <tr ng-show="cs.extra"><td colspan="2" class="alert ng-binding">Default is greedy. Append ? for reluctant.</td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Groups</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(...)</td><td class="ng-binding">Capturing group</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?P&lt;Y&gt;...)</td><td class="ng-binding">Capturing group named Y</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?:...)</td><td class="ng-binding">Non-capturing group</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\Y</td><td class="ng-binding">Match the Y'th captured group</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?P=Y)</td><td class="ng-binding">Match the named group Y</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?#...)</td><td class="ng-binding">Comment</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table>
    </td><td ng-repeat="col in cheatsheets" class="bigrow ng-scope">
      <!-- ngRepeat: cs in col --><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Character Classes</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">[ab-d]</td><td class="ng-binding">One character of: a, b, c, d</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">[^ab-d]</td><td class="ng-binding">One character except: a, b, c, d</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">[\b]</td><td class="ng-binding">Backspace character</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\d</td><td class="ng-binding">One digit</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\D</td><td class="ng-binding">One non-digit</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\s</td><td class="ng-binding">One whitespace</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\S</td><td class="ng-binding">One non-whitespace</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\w</td><td class="ng-binding">One word character</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\W</td><td class="ng-binding">One non-word character</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Assertions</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">^</td><td class="ng-binding">Start of string</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\A</td><td class="ng-binding">Start of string, ignores m flag</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">$</td><td class="ng-binding">End of string</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\Z</td><td class="ng-binding">End of string, ignores m flag</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\b</td><td class="ng-binding">Word boundary</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\B</td><td class="ng-binding">Non-word boundary</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?=...)</td><td class="ng-binding">Positive lookahead</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?!...)</td><td class="ng-binding">Negative lookahead</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?&lt;=...)</td><td class="ng-binding">Positive lookbehind</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?&lt;!...)</td><td class="ng-binding">Negative lookbehind</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?()|)</td><td class="ng-binding">Conditional</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope ng-hide" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Escapes</th></tr>
        <!-- ngRepeat: v in filtList -->
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table>
    </td><td ng-repeat="col in cheatsheets" class="bigrow ng-scope">
      <!-- ngRepeat: cs in col --><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Flags</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">i</td><td class="ng-binding">Ignore case</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">m</td><td class="ng-binding">^ and $ match start and end of line</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">s</td><td class="ng-binding">. matches newline as well</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">x</td><td class="ng-binding">Allow spaces and comments</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">L</td><td class="ng-binding">Locale character classes</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">u</td><td class="ng-binding">Unicode character classes</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">(?iLmsux)</td><td class="ng-binding">Set flags within regex</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Special Characters</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\n</td><td class="ng-binding">Newline</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\r</td><td class="ng-binding">Carriage return</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\t</td><td class="ng-binding">Tab</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\YYY</td><td class="ng-binding">Octal character YYY</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\xYY</td><td class="ng-binding">Hexadecimal character YY</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope ng-hide" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Posix Classes</th></tr>
        <!-- ngRepeat: v in filtList -->
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table><table class="mini-cheatsheet ng-scope" ng-repeat="cs in col" ng-show="filtList = (cs.list | filter:{2:flavorModel.val} | filter:filterModel.val);filtList.length">
        <tbody><tr><th colspan="2" class="ng-binding">Regular Expression Replacement</th></tr>
        <!-- ngRepeat: v in filtList --><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\g&lt;0&gt;</td><td class="ng-binding">Insert entire match</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\g&lt;Y&gt;</td><td class="ng-binding">Insert match Y (name or number)</td></tr><tr ng-repeat="v in filtList" class="ng-scope">
          <td style="white-space:nowrap" class="ng-binding">\Y</td><td class="ng-binding">Insert group numbered Y</td></tr>
        
        <tr ng-show="cs.extra" class="ng-hide"><td colspan="2" class="alert ng-binding"></td></tr>
      </tbody></table>
    </td>
  </tr></tbody></table>