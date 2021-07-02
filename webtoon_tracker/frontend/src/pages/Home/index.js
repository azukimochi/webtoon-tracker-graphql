import React, { useEffect } from 'react'
import Axios from 'axios'
import { startCase } from 'lodash'
import { makeStyles,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow } from '@material-ui/core'
import { webtoonFields, parseData } from '../../utils'

const columns = webtoonFields.map(field => ({
  id: field,
  label: startCase(field),
  minWidth: 170,
  align: 'left',
  value: (value) => formatCellValue(value)
}))

const formatCellValue = (value) => {
  switch(typeof value) {
    case 'boolean':
      console.log(value, 'hit this 1')
      return value ? <div>&#10003;</div> : <div>&#10007;</div>
    case 'object':
      console.log(value, 'hit this 2')
      return value.constructor === Array ? value.map(val => (<div>{val?.username || val?.dayOfWeek}</div>)) : null
    default:
      console.log(value, 'hit this 3')
      return value
  }
}
const useStyles = makeStyles({
  root: {
    width: '100%',
  },
  container: {
    maxHeight: 440,
  },
});


const Home = () => {
    const classes = useStyles();
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(10);
    const [rows, setRows] = React.useState([])

    useEffect(() => {
      const fetchAllWebtoons = async () => {
        const data = {
          query: `query {
            allWebtoons {
              edges {
                node {
                  id
                  title
                  completedReading
                  dropped
                  daysOfRelease {
                    edges {
                      node {
                        id
                        dayOfWeek
                      }
                    }
                  }
                  authors {
                    edges {
                      node {
                        id
                        username
                      }
                    }
                  }
                }
              }
            }
          }`
        }
        const { data: response } = await Axios.post('/api/graphql', data)
        const edges = response.data.allWebtoons.edges
        console.log('Karen webtoons: ', edges)
        console.log('Karen parsed: ', parseData(edges))
        setRows(parseData(edges))
      }
      fetchAllWebtoons()
    }, [])

    const handleChangePage = (event, newPage) => {
      setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
      setRowsPerPage(+event.target.value);
      setPage(0);
    };

    return (
      <Paper className={classes.root}>
        <TableContainer className={classes.container}>
          <Table stickyHeader aria-label="sticky table">
            <TableHead>
              <TableRow>
                {columns.map((column) => (
                  <TableCell
                    key={column.id}
                    align={column.align}
                    style={{ minWidth: column.minWidth }}
                  >
                    {column.label}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.id}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      console.log('Karen value: ', value)
                      return (
                        <TableCell key={column.id} align={column.align}>
                          {column.value(value)}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[10, 25, 100]}
          component="div"
          count={rows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onChangePage={handleChangePage}
          onChangeRowsPerPage={handleChangeRowsPerPage}
        />
      </Paper>
    );
}

export default Home