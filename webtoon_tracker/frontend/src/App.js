import React, { Suspense } from 'react'
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom'

const Home = React.lazy(() => import('./pages/Home'))
const A = React.lazy(() => import('./pages/A'))
const B = React.lazy(() => import('./pages/B'))

const App = () => (
    <Router>
        <Suspense fallback={<div>....Something</div>}>
        <div id="test">
        <Link to="/">All Data</Link>
        <Link to="/a">A</Link>
        <Link to="/b">B</Link>
        </div>
        <Switch>
            <Route path="/" component={Home} exact />
            <Route path="/a" component={A} />
            <Route path="/b" component={B} />
        </Switch>
        </Suspense>
    </Router>
)

export default App