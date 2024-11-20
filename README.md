## DWVCK-ext (Download WV Clearkeys Extension)

DecosSoft slightly modified version of <a href="https://github.com/FoxRefire/wvg/archive/refs/heads/next.zip">FoxRefire's</a> extension.
                                   

### Installation

1. Download or clone this code
2. At the same directory of `manifest.json`(root directory of this extension), put the one of the following Android L3 CDM key pair file(s).

   * Supported CDM Key Pair Formats

      1. `device.wvd`

      2. `device_client_id_blob` + `device_private_key`

      3. `client_id.bin` + `private_key.pem`

      4. `remote.json`
         
3. Install extension
   
   * Firefox
          
     1\. Navigate to `about:debugging#/runtime/this-firefox`
     
     2\. Load temporary addon
   
   * Chrome

     1\. Navigate to `chrome://extensions/`

     2\. Load unpacked

   * Kiwi Browser(Android)

     1\. Navigate to ︙ --> Extensions

     2\. \+(from .zip/.crx/.user.js)
