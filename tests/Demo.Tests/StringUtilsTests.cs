using Demo;

using Xunit;

namespace Demo.Tests;

public sealed class StringUtilsTests
{
    [Fact]
    public void Reverse_DaoNguocChuoi() => Assert.Equal("cba", StringUtils.Reverse("abc"));

    [Fact]
    public void Reverse_ChuoiRong_TraVeChuoiRong() => Assert.Equal(string.Empty, StringUtils.Reverse(""));

    [Fact]
    public void Reverse_Null_NemArgumentNullException() =>
        Assert.Throws<ArgumentNullException>(() => StringUtils.Reverse(null!));
}
