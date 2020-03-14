# Create MD5 sums of output files from the pipeline

rm -f output_files.txt
touch output_files.txt

find output_dir/ \
  -type f \
  -name results.txt \
  >> output_files.txt

find output_dir/random_samples \
  -type f \
  -name \* \
  >> output_files.txt

md5sum $(cat output_files.txt)