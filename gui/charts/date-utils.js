export function formatDate(series){
  series.forEach(item => {
    item.data.forEach(dataPoint => {
      dataPoint[0] = new Date(dataPoint[0]).getTime();
    });
  });
}