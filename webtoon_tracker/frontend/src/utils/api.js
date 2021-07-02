export const parseData = edges => {
    return edges.reduce((arr, { node }) => {
        for (const key in node) {
            if (node[key]?.edges && node[key].edges.constructor === Array) {
                node[key] = parseData(node[key].edges)
            }
        }
        arr.push(node)
        return arr
    }, [])
}