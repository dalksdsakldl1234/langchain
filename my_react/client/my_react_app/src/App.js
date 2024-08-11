import Customer from './Customer'
import './App.css'
import Table from '@material-ui/core/Table'
import TableHead from '@material-ui/core/TableHead'
import TableBody from '@material-ui/core/TableBody'
import TableRow from '@material-ui/core/TableRow'
import TableCell from '@material-ui/core/TableCell'


const customer = {
  'name' : '하태웅',
  'id' : '32204797'
}
function App() {
  return (
    <div>
      <Customer name = {customer.name} id = {customer.id}/>
    </div>
  );
}

export default App;
