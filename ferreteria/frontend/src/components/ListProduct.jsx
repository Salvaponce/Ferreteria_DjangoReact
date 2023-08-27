function ListProduct(props){
      function handleClick(){
    props.deletion(props.id)
  }
    return (
        <div className="note">
          <h1 >  Title: {props.name} </h1>
          <p > Content: {props.descripcion}</p>
          <button onClick={handleClick}>Delete</button>
        </div>
    )
  }

export default ListProduct;

