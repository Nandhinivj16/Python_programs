/**
 * @file stats.c
 * @brief Statistical analysis of a data set
 *
 * The program sorts a test array, computes its minimum, maximum,
 * mean and median, and prints the results.
 *
 * @author Your Name
 * @date October 2026
 */
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include "stats.h"

#define SIZE (40)

int main(int argc, char *argv[])
{
  unsigned char test[SIZE];
  if (argc < 2)
  {
    printf("Error: Please provide at least one input.\n");
    return 1;
  }

  if (argc > SIZE + 1)
  {
    printf("Error: Maximum 40 input values allowed.\n");
    return 1;
  }

  unsigned int length = argc - 1;

  for (unsigned int i = 0; i < length; i++)
  {
    char *endptr;
    long value;

    errno = 0;
    value = strtol(argv[i + 1], &endptr, 10);

    if (endptr == argv[i + 1] || *endptr != '\0' ||
        errno == ERANGE || value < 0 || value > UCHAR_MAX)
    {
      printf("Invalid input: %s\n", argv[i + 1]);
      return 1;
    }

    test[i] = (unsigned char)value;
  }

  printf("Original array:\n");
  print_array(test, length);

  sort_array(test, length);
  printf("\nSorted array (largest to smallest):\n");
  print_array(test, length);

  print_statistics(find_minimum(test, length),
                   find_maximum(test, length),
                   find_mean(test, length),
                   find_median(test, length));
  return 0;
}

void print_statistics(unsigned char min, unsigned char max,
                      unsigned char mean, unsigned char median)
{
  printf("\nStatistics:\n");
  printf("  Minimum: %u\n", min);
  printf("  Maximum: %u\n", max);
  printf("  Mean: %u\n", mean);
  printf("  Median: %u\n", median);
}

void print_array(unsigned char *array, unsigned int length)
{
  unsigned int i;
  for (i = 0; i < length; i++)
  {
    printf("%3u", array[i]);
    printf((i + 1) % 10 == 0 ? "\n" : " ");
  }
  if (length % 10 != 0)
  {
    printf("\n");
  }
}

void sort_array(unsigned char *array, unsigned int length)
{
  unsigned int i, j;
  unsigned char tmp;
  for (i = 0; i + 1 < length; i++)
  {
    for (j = 0; j + 1 < length - i; j++)
    {
      if (array[j] < array[j + 1])
      {
        tmp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = tmp;
      }
    }
  }
}

unsigned char find_median(unsigned char *array, unsigned int length)
{
  unsigned int mid;
  if (length == 0)
  {
    return 0;
  }
  sort_array(array, length);
  mid = length / 2;
  if (length % 2 == 0)
  {
    return (unsigned char)(((unsigned int)array[mid - 1] + array[mid]) / 2);
  }
  return array[mid];
}

unsigned char find_mean(unsigned char *array, unsigned int length)
{
  unsigned int i, sum = 0;
  if (length == 0)
  {
    return 0;
  }
  for (i = 0; i < length; i++)
  {
    sum += array[i];
  }
  return (unsigned char)(sum / length);
}

unsigned char find_maximum(unsigned char *array, unsigned int length)
{
  unsigned int i;
  unsigned char max;
  if (length == 0)
  {
    return 0;
  }
  max = array[0];
  for (i = 1; i < length; i++)
  {
    if (array[i] > max)
    {
      max = array[i];
    }
  }
  return max;
}

unsigned char find_minimum(unsigned char *array, unsigned int length)
{
  unsigned int i;
  unsigned char min;
  if (length == 0)
  {
    return 0;
  }
  min = array[0];
  for (i = 1; i < length; i++)
  {
    if (array[i] < min)
    {
      min = array[i];
    }
  }
  return min;
}
