/* eslint-disable */

export function unSlugify(data, replaceValue, replaceWith) {
    // replaces all occurances of replaceValue if present else replaces hyphens (-)
    // with the supplied replaceWith value if present else replace with spaces
    const value = data.replaceAll(replaceValue?? "-", replaceWith?? " ")

    return { value }
}