import { useMemo } from "react";

const filterByOccurrenceAtIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.charAt(index) === char;
  });
};

const filterByNonOccurrenceAtIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.charAt(index) !== char;
  });
};

const filterByIncludesWithWrongIndex = (index, char, words) => {
  return words.filter((word) => {
    return word.includes(char) && word.charAt(index) !== char;
  });
};

// Hook
export function filterAPI() {
  // Return our custom router object
  // Memoize so that a new object is only returned if something changes
  return {
    byOccurence: filterByOccurrenceAtIndex,
    byNonOccurence: filterByNonOccurrenceAtIndex,
    byOccurrenceAtDifferentIndex: filterByIncludesWithWrongIndex,
  };
}
