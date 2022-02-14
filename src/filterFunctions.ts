
export const filterByOccurrenceAtIndex = ( index:number, char:string, words: string[]) => {
    return words.filter( (word)=> {
        return (word.charAt(index) === char);
    })
}

export const filterByNonOccurrenceAtIndex = ( index:number, char:string, words: string[]) => {
    return words.filter( (word)=> {
        return (word.charAt(index) !== char);
    })
}

export const filterByIncludesWithWrongIndex = ( index:number, char:string, words: string[]) => {
    return words.filter( (word)=> {
        return (word.includes(char) && (word.charAt(index) !== char));
    })
}

