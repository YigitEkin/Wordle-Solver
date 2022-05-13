export const filterByOccurrenceAtIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.charAt(index) === char;
  });
};

export const filterByNonOccurrenceAtIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.charAt(index) !== char;
  });
};

export const filterByIncludesWithWrongIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.includes(char) && word.charAt(index) !== char;
  });
};
