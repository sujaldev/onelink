const ErrorPage = ({ err }) => {
  return (
    <div className="error-page">
      <h1>OOPS Error!!</h1>
      <h1>{Messages[err]}</h1>
    </div>
  );
};
const Messages = ["User Not Found", "Invalid URL"];

export default ErrorPage;
