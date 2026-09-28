<?php
$files_to_delete = [
    '../index.html',
    '../team.html',
    '../treatments.html',
];

// Delete all treatment-*.html
$treatment_files = glob('../treatment-*.html');
if ($treatment_files) {
    $files_to_delete = array_merge($files_to_delete, $treatment_files);
}

$deleted = 0;
foreach ($files_to_delete as $file) {
    if (file_exists($file)) {
        unlink($file);
        $deleted++;
    }
}

echo "Cleanup complete! Successfully deleted $deleted old HTML files. Your site is now fully running on the dynamic PHP system!";
?>
